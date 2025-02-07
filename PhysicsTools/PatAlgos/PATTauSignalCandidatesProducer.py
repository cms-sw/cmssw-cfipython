import FWCore.ParameterSet.Config as cms

def PATTauSignalCandidatesProducer(*args, **kwargs):
  mod = cms.EDProducer('PATTauSignalCandidatesProducer',
    src = cms.InputTag('slimmedTaus'),
    storeLostTracks = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
