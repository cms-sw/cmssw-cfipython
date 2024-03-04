import FWCore.ParameterSet.Config as cms

def CorrectedTrackJetProducer(**kwargs):
  mod = cms.EDProducer('CorrectedTrackJetProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
