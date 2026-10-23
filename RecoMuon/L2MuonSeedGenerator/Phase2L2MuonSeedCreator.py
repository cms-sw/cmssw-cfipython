import FWCore.ParameterSet.Config as cms

def Phase2L2MuonSeedCreator(*args, **kwargs):
  mod = cms.EDProducer('Phase2L2MuonSeedCreator',
    inputObjects = cms.InputTag('l1tTkMuonsGmt'),
    cscRecSegmentLabel = cms.InputTag('hltCscSegments'),
    dtRecSegmentLabel = cms.InputTag('hltDt4DSegments'),
    minPL1Tk = cms.double(3.5),
    maxPL1Tk = cms.double(200),
    stubMatchDPhi = cms.double(0.05),
    stubMatchDTheta = cms.double(0.1),
    extrapolationWindowClose = cms.double(0.1),
    extrapolationWindowFar = cms.double(0.05),
    maximumEtaBarrel = cms.double(0.7),
    maximumEtaOverlap = cms.double(1.3),
    propagator = cms.string('SteppingHelixPropagatorAny'),
    serviceParameters = cms.PSet(
      Propagators = cms.untracked.vstring('SteppingHelixPropagatorAny'),
      RPCLayers = cms.bool(True),
      UseMuonNavigation = cms.untracked.bool(True)
    ),
    estimatorMaxChi2 = cms.double(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
