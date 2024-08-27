import FWCore.ParameterSet.Config as cms

def FFTPileupRhoEtaDependenceTableESProducer(**kwargs):
  mod = cms.ESProducer('FFTPileupRhoEtaDependenceTableESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
