import FWCore.ParameterSet.Config as cms

ctppsBeamParametersFromLHCInfoESSource = cms.ESProducer('CTPPSBeamParametersFromLHCInfoESSource',
  lhcInfoLabel = cms.string(''),
  beamDivX45 = cms.double(0.1),
  beamDivY45 = cms.double(0.1),
  beamDivX56 = cms.double(0.1),
  beamDivY56 = cms.double(0.1),
  vtxOffsetX45 = cms.double(0.01),
  vtxOffsetY45 = cms.double(0.01),
  vtxOffsetZ45 = cms.double(0.01),
  vtxOffsetX56 = cms.double(0.01),
  vtxOffsetY56 = cms.double(0.01),
  vtxOffsetZ56 = cms.double(0.01),
  vtxStddevX = cms.double(0.02),
  vtxStddevY = cms.double(0.02),
  vtxStddevZ = cms.double(0.02),
  appendToDataLabel = cms.string('')
)
