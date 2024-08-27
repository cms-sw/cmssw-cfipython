import FWCore.ParameterSet.Config as cms

def PATTauSignalCandidatesProducer(**kwargs):
  mod = cms.EDProducer('PATTauSignalCandidatesProducer',
    src = cms.InputTag('slimmedTaus'),
    storeLostTracks = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
