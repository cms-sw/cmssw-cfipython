import FWCore.ParameterSet.Config as cms

def PackedCandMCMatchTableProducer(*args, **kwargs):
  mod = cms.EDProducer('PackedCandMCMatchTableProducer',
    objName = cms.required.string,
    branchName = cms.required.string,
    docString = cms.required.string,
    src = cms.required.InputTag,
    genparticles = cms.optional.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
