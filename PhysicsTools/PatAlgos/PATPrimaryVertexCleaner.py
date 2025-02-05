import FWCore.ParameterSet.Config as cms

def PATPrimaryVertexCleaner(*args, **kwargs):
  mod = cms.EDFilter('PATPrimaryVertexCleaner',
    src = cms.InputTag(''),
    minMultiplicity = cms.uint32(1),
    minPtSum = cms.double(0),
    maxTrackEta = cms.double(9999),
    maxNormChi2 = cms.double(9999),
    maxDeltaR = cms.double(9999),
    maxDeltaZ = cms.double(9999),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
