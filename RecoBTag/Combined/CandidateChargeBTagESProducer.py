import FWCore.ParameterSet.Config as cms

def CandidateChargeBTagESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateChargeBTagESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
