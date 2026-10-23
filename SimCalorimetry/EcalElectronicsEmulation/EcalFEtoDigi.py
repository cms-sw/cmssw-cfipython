import FWCore.ParameterSet.Config as cms

def EcalFEtoDigi(*args, **kwargs):
  mod = cms.EDProducer('EcalFEtoDigi',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
