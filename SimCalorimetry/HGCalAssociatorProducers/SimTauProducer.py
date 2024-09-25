import FWCore.ParameterSet.Config as cms

def SimTauProducer(*args, **kwargs):
  mod = cms.EDProducer('SimTauProducer',
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    genParticles = cms.InputTag('genParticles'),
    genBarcodes = cms.InputTag('genParticles'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
