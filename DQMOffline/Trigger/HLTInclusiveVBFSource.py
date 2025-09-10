import FWCore.ParameterSet.Config as cms

def HLTInclusiveVBFSource(*args, **kwargs):
  mod = cms.EDProducer('HLTInclusiveVBFSource',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
