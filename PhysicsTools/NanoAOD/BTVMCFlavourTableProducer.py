import FWCore.ParameterSet.Config as cms

def BTVMCFlavourTableProducer(**kwargs):
  mod = cms.EDProducer('BTVMCFlavourTableProducer',
    src = cms.required.InputTag,
    genparticles = cms.required.InputTag,
    name = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
