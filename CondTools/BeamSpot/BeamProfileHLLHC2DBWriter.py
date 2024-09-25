import FWCore.ParameterSet.Config as cms

def BeamProfileHLLHC2DBWriter(*args, **kwargs):
  mod = cms.EDAnalyzer('BeamProfileHLLHC2DBWriter',
    recordName = cms.string('SimBeamSpotHLLHCObjectsRcd'),
    MeanX = cms.double(0),
    MeanY = cms.double(0),
    MeanZ = cms.double(0),
    EProton = cms.double(0),
    CrabFrequency = cms.double(0),
    RF800 = cms.double(0),
    CrossingAngle = cms.double(0),
    CrabbingAngleCrossing = cms.double(0),
    CrabbingAngleSeparation = cms.double(0),
    BetaCrossingPlane = cms.double(0),
    BetaSeparationPlane = cms.double(0),
    HorizontalEmittance = cms.double(0),
    VerticalEmittance = cms.double(0),
    BunchLength = cms.double(0),
    TimeOffset = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
