import FWCore.ParameterSet.Config as cms

def TrackMultiplicityFilter(*args, **kwargs):
  mod = cms.EDFilter('TrackMultiplicityFilter',
    trackInputTag = cms.untracked.InputTag('generalTracks'),
    cut = cms.untracked.string(''),
    nmin = cms.untracked.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
