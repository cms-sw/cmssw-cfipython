import FWCore.ParameterSet.Config as cms

def BTVMCFlavourTableProducer(*args, **kwargs):
  mod = cms.EDProducer('BTVMCFlavourTableProducer',
    src = cms.required.InputTag,
    genparticles = cms.required.InputTag,
    name = cms.required.string,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
