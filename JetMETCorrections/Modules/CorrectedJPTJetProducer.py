import FWCore.ParameterSet.Config as cms

def CorrectedJPTJetProducer(**kwargs):
  mod = cms.EDProducer('CorrectedJPTJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
