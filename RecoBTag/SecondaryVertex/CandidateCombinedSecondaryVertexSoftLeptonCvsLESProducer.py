import FWCore.ParameterSet.Config as cms

def CandidateCombinedSecondaryVertexSoftLeptonCvsLESProducer(**kwargs):
  mod = cms.ESProducer('CandidateCombinedSecondaryVertexSoftLeptonCvsLESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
