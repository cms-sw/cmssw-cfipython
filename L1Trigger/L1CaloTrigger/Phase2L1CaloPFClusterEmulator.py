import FWCore.ParameterSet.Config as cms

def Phase2L1CaloPFClusterEmulator(*args, **kwargs):
  mod = cms.EDProducer('Phase2L1CaloPFClusterEmulator',
    gctFullTowers = cms.InputTag('l1tPhase2L1CaloEGammaEmulator', 'GCTFullTowers'),
    hcalDigis = cms.InputTag('simHcalTriggerPrimitiveDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
