import FWCore.ParameterSet.Config as cms

def TrackMultiplicityFilter(**kwargs):
  mod = cms.EDFilter('TrackMultiplicityFilter',
    trackInputTag = cms.untracked.InputTag('generalTracks'),
    cut = cms.untracked.string(''),
    nmin = cms.untracked.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
