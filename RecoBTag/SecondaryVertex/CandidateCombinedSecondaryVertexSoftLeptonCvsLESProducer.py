import FWCore.ParameterSet.Config as cms

def CandidateCombinedSecondaryVertexSoftLeptonCvsLESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateCombinedSecondaryVertexSoftLeptonCvsLESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
