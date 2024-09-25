import FWCore.ParameterSet.Config as cms

def JetFlavourIdentifier(*args, **kwargs):
  mod = cms.EDProducer('JetFlavourIdentifier',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
