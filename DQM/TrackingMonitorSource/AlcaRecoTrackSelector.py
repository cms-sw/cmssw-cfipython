import FWCore.ParameterSet.Config as cms

def AlcaRecoTrackSelector(*args, **kwargs):
  mod = cms.EDProducer('AlcaRecoTrackSelector',
    trackInputTag = cms.untracked.InputTag('generalTracks'),
    ptmin = cms.untracked.double(0),
    pmin = cms.untracked.double(0),
    etamin = cms.untracked.double(-4),
    etamax = cms.untracked.double(4),
    nhits = cms.untracked.uint32(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
