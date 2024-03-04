import FWCore.ParameterSet.Config as cms

def CombinedSecondaryVertexSoftLeptonESProducer(**kwargs):
  mod = cms.ESProducer('CombinedSecondaryVertexSoftLeptonESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
