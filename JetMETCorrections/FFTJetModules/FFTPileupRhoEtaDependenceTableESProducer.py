import FWCore.ParameterSet.Config as cms

def FFTPileupRhoEtaDependenceTableESProducer(*args, **kwargs):
  mod = cms.ESProducer('FFTPileupRhoEtaDependenceTableESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
