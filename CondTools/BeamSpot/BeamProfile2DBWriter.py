import FWCore.ParameterSet.Config as cms

def BeamProfile2DBWriter(**kwargs):
  mod = cms.EDAnalyzer('BeamProfile2DBWriter',
    recordName = cms.string('SimBeamSpotObjectsRcd'),
    X0 = cms.double(0),
    Y0 = cms.double(0),
    Z0 = cms.double(0),
    MeanX = cms.double(0),
    MeanY = cms.double(0),
    MeanZ = cms.double(0),
    SigmaX = cms.double(-1),
    SigmaY = cms.double(-1),
    SigmaZ = cms.double(0),
    BetaStar = cms.double(0),
    Emittance = cms.double(0),
    Alpha = cms.double(0),
    Phi = cms.double(0),
    TimeOffset = cms.double(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
