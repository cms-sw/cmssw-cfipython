import FWCore.ParameterSet.Config as cms

def HLTMuonPointingFilter(*args, **kwargs):
  mod = cms.EDFilter('HLTMuonPointingFilter',
    SALabel = cms.InputTag('hltCosmicMuonBarrelOnly'),
    PropagatorName = cms.string('SteppingHelixPropagatorAny'),
    radius = cms.double(90),
    maxZ = cms.double(280),
    PixHits = cms.uint32(0),
    TkLayers = cms.uint32(0),
    MuonHits = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
