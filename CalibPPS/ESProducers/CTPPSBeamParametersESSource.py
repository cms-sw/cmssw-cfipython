import FWCore.ParameterSet.Config as cms

def CTPPSBeamParametersESSource(**kwargs):
  mod = cms.ESSource('CTPPSBeamParametersESSource',
    setBeamPars = cms.bool(True),
    beamMom45 = cms.double(6500),
    beamMom56 = cms.double(6500),
    betaStarX45 = cms.double(30),
    betaStarY45 = cms.double(30),
    betaStarX56 = cms.double(30),
    betaStarY56 = cms.double(30),
    beamDivX45 = cms.double(0.1),
    beamDivY45 = cms.double(0.1),
    beamDivX56 = cms.double(0.1),
    beamDivY56 = cms.double(0.1),
    halfXangleX45 = cms.double(8e-05),
    halfXangleY45 = cms.double(8e-05),
    halfXangleX56 = cms.double(8e-05),
    halfXangleY56 = cms.double(8e-05),
    vtxOffsetX45 = cms.double(0.01),
    vtxOffsetY45 = cms.double(0.01),
    vtxOffsetZ45 = cms.double(0.01),
    vtxOffsetT45 = cms.double(0.01),
    vtxOffsetX56 = cms.double(0.01),
    vtxOffsetY56 = cms.double(0.01),
    vtxOffsetZ56 = cms.double(0.01),
    vtxOffsetT56 = cms.double(0.01),
    vtxStddevX = cms.double(0.02),
    vtxStddevY = cms.double(0.02),
    vtxStddevZ = cms.double(0.02),
    vtxStddevT = cms.double(0.02),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
