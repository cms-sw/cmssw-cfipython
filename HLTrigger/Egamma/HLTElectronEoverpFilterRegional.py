import FWCore.ParameterSet.Config as cms

def HLTElectronEoverpFilterRegional(*args, **kwargs):
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
