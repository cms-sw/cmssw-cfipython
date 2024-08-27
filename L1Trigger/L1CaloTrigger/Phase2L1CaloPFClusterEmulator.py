import FWCore.ParameterSet.Config as cms

def Phase2L1CaloPFClusterEmulator(**kwargs):
  mod = cms.EDProducer('Phase2L1CaloPFClusterEmulator',
    gctFullTowers = cms.InputTag('l1tPhase2L1CaloEGammaEmulator', 'GCTFullTowers'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
