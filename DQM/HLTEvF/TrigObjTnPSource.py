import FWCore.ParameterSet.Config as cms

def TrigObjTnPSource(*args, **kwargs):
  mod = cms.EDProducer('TrigObjTnPSource',
    triggerEvent = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    triggerResults = cms.InputTag('TriggerResults', '', 'HLT'),
    histColls = cms.VPSet(
      template = cms.PSetTemplate(
        tagCuts = cms.VPSet(
          template = cms.PSetTemplate(
            rangeVar = cms.string(''),
            allowedRanges = cms.vstring()
          )
        ),
        probeCuts = cms.VPSet(
          template = cms.PSetTemplate(
            rangeVar = cms.string(''),
            allowedRanges = cms.vstring()
          )
        ),
        tagFilters = cms.PSet(
          filterSets = cms.VPSet(
            template = cms.PSetTemplate(
              filters = cms.vstring(),
              isAND = cms.bool(True)
            )
          ),
          isAND = cms.bool(False)
        ),
        collName = cms.string('stdTag'),
        folderName = cms.string('HLT/EGM/TrigObjTnP'),
        histDefs = cms.PSet(
          configs = cms.VPSet(
            template = cms.PSetTemplate(
              filler = cms.PSet(
                localCuts = cms.required.VPSet,
                var = cms.string('pt')
              ),
              bins = cms.vdouble(
                -2.5,
                -1.5,
                0,
                1.5,
                2.5
              ),
              nameSuffex = cms.string('_eta'),
              titleSuffex = cms.string(';#eta;mass [GeV]')
            )
          ),
          massBins = cms.vdouble(
            60,
            61,
            62,
            63,
            64,
            65,
            66,
            67,
            68,
            69,
            70,
            71,
            72,
            73,
            74,
            75,
            76,
            77,
            78,
            79,
            80,
            81,
            82,
            83,
            84,
            85,
            86,
            87,
            88,
            89,
            90,
            91,
            92,
            93,
            94,
            95,
            96,
            97,
            98,
            99,
            100,
            101,
            102,
            103,
            104,
            105,
            106,
            107,
            108,
            109,
            110,
            111,
            112,
            113,
            114,
            115,
            116,
            117,
            118,
            119,
            120
          )
        ),
        probeFilters = cms.vstring(),
        evtTrigSel = cms.PSet(
          selectionStr = cms.string(''),
          isANDForExpandedPaths = cms.bool(False),
          verbose = cms.int32(1)
        )
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
