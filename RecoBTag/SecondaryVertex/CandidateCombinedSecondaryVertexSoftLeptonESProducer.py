import FWCore.ParameterSet.Config as cms

def CandidateCombinedSecondaryVertexSoftLeptonESProducer(*args, **kwargs):
  mod = cms.ESProducer('CandidateCombinedSecondaryVertexSoftLeptonESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
