import FWCore.ParameterSet.Config as cms

def HLTElectronGenericFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTElectronGenericFilter',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('hltSingleElectronOneOEMinusOneOPFilter'),
    varTag = cms.InputTag('hltSingleElectronTrackIsol'),
    lessThan = cms.bool(True),
    thrRegularEB = cms.double(0),
    thrRegularEE = cms.double(0),
    thrOverPtEB = cms.double(-1),
    thrOverPtEE = cms.double(-1),
    thrTimesPtEB = cms.double(-1),
    thrTimesPtEE = cms.double(-1),
    ncandcut = cms.int32(1),
    l1EGCand = cms.InputTag('hltPixelMatchElectronsL1Iso'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
