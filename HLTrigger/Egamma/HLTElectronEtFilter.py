import FWCore.ParameterSet.Config as cms

def HLTElectronEtFilter(**kwargs):
  mod = cms.EDFilter('HLTElectronEtFilter',
    saveTags = cms.bool(True),
    candTag = cms.InputTag('hltElectronPixelMatchFilter'),
    EtCutEB = cms.double(0),
    EtCutEE = cms.double(0),
    ncandcut = cms.int32(1),
    l1EGCand = cms.InputTag('hltL1IsoRecoEcalCandidate'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
