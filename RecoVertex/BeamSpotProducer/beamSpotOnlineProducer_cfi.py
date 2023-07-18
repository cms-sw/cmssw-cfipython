import FWCore.ParameterSet.Config as cms

beamSpotOnlineProducer = cms.EDProducer('BeamSpotOnlineProducer',
  changeToCMSCoordinates = cms.bool(False),
  maxZ = cms.double(40),
  setSigmaZ = cms.double(-1),
  beamMode = cms.untracked.uint32(11),
  src = cms.InputTag('hltScalersRawToDigi'),
  gtEvmLabel = cms.InputTag(''),
  maxRadius = cms.double(2),
  useTransientRecord = cms.bool(False),
  mightGet = cms.optional.untracked.vstring
)
