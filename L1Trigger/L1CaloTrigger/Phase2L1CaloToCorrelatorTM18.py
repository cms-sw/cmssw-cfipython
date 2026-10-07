import FWCore.ParameterSet.Config as cms

def Phase2L1CaloToCorrelatorTM18(*args, **kwargs):
  mod = cms.EDProducer('Phase2L1CaloToCorrelatorTM18',
    gctEmDigiClusters = cms.InputTag('l1tPhase2GCTBarrelToCorrelatorLayer1Emulator', 'GCTEmDigiClusters'),
    gctHadDigiClusters = cms.InputTag('l1tPhase2GCTBarrelToCorrelatorLayer1Emulator', 'GCTHadDigiClusters'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
