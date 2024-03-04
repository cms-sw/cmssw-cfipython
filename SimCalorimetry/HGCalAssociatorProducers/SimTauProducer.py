import FWCore.ParameterSet.Config as cms

def SimTauProducer(**kwargs):
  mod = cms.EDProducer('SimTauProducer',
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    genParticles = cms.InputTag('genParticles'),
    genBarcodes = cms.InputTag('genParticles'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
