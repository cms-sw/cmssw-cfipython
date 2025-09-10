import FWCore.ParameterSet.Config as cms

def ColinsSoperVariablesComputer(*args, **kwargs):
  mod = cms.EDProducer('ColinsSoperVariablesComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
