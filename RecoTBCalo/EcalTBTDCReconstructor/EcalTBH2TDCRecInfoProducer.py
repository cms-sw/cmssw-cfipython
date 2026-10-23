import FWCore.ParameterSet.Config as cms

def EcalTBH2TDCRecInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalTBH2TDCRecInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
