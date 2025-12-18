import FWCore.ParameterSet.Config as cms

def FourVectorHLT(*args, **kwargs):
  mod = cms.EDProducer('FourVectorHLT',
    plotAll = cms.untracked.bool(False),
    Nbins = cms.untracked.uint32(50),
    ptMin = cms.untracked.double(0),
    ptMax = cms.untracked.double(200),
    filters = cms.VPSet(
      template = cms.PSetTemplate(
        name = cms.string(''),
        type = cms.int32(0),
        ptMin = cms.untracked.double(0),
        ptMax = cms.untracked.double(200)
      )
    ),
    triggerSummaryLabel = cms.InputTag('hltTriggerSummaryAOD', '', 'HLT'),
    topFolderName = cms.untracked.string('HLT/FourVectorHLT'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
