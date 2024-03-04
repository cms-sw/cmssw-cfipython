import FWCore.ParameterSet.Config as cms

def HLTElectronEoverpFilterRegional(**kwargs):
  mod = cms.EDFilter('HLTElectronEoverpFilterRegional',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('hltElectronPixelMatchFilter'),
    electronIsolatedProducer = cms.InputTag('pixelMatchElectronsForHLT'),
    electronNonIsolatedProducer = cms.InputTag('pixelMatchElectronsForHLT'),
    eoverpbarrelcut = cms.double(1.5),
    eoverpendcapcut = cms.double(2.45),
    ncandcut = cms.int32(1),
    doIsolated = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
