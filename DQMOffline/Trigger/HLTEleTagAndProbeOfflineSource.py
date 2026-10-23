import FWCore.ParameterSet.Config as cms

def HLTEleTagAndProbeOfflineSource(*args, **kwargs):
  mod = cms.EDProducer('HLTEleTagAndProbeOfflineSource',
    tagAndProbeCollections = cms.VPSet(
      template = cms.PSetTemplate(
        tagRangeCuts = cms.VPSet(
          template = cms.PSetTemplate(
            rangeVar = cms.string(''),
            allowedRanges = cms.vstring()
          )
        ),
        probeRangeCuts = cms.VPSet(
          template = cms.PSetTemplate(
            rangeVar = cms.string(''),
            allowedRanges = cms.vstring()
          )
        ),
        trigEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
        tagColl = cms.InputTag(''),
        probeColl = cms.InputTag(''),
        tagVIDCuts = cms.InputTag(''),
        probeVIDCuts = cms.InputTag(''),
        tagFilters = cms.vstring(),
        probeFilters = cms.vstring(),
        tagFiltersORed = cms.bool(True),
        probeFiltersORed = cms.bool(False),
        minTagProbeDR = cms.double(0),
        minMass = cms.required.double,
        maxMass = cms.required.double,
        requireOpSign = cms.required.bool,
        histConfigs = cms.VPSet(
          template = cms.PSetTemplate(
            histType = cms.string('1D'),
            binLowEdges = cms.vdouble(),
            nameSuffex = cms.string(''),
            vsVar = cms.string(''),
            rangeCuts = cms.VPSet(
              template = cms.PSetTemplate(
                rangeVar = cms.string(''),
                allowedRanges = cms.vstring()
              )
            )
          )
        ),
        filterConfigs = cms.VPSet(
          template = cms.PSetTemplate(
            rangeCuts = cms.VPSet(
              template = cms.PSetTemplate(
                rangeVar = cms.string(''),
                allowedRanges = cms.vstring()
              )
            ),
            filterName = cms.string(''),
            histTitle = cms.string(''),
            folderName = cms.string(''),
            tagExtraFilter = cms.string('')
          )
        ),
        baseHistName = cms.required.string,
        sampleTrigRequirements = cms.PSet(
          andOr = cms.bool(False),
          verbosityLevel = cms.uint32(1),
          andOrDcs = cms.bool(False),
          dcsInputTag = cms.InputTag('scalersRawToDigi'),
          dcsRecordInputTag = cms.InputTag('onlineMetaDataDigis'),
          dcsPartitions = cms.vint32(
            24,
            25,
            26,
            27,
            28,
            29
          ),
          errorReplyDcs = cms.bool(True),
          dbLabel = cms.string(''),
          andOrHlt = cms.bool(True),
          hltInputTag = cms.InputTag('TriggerResults', '', 'HLT'),
          hltPaths = cms.vstring(),
          hltDBKey = cms.string(''),
          errorReplyHlt = cms.bool(False)
        )
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
