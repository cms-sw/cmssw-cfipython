import FWCore.ParameterSet.Config as cms

def BeamSpotOnlineProducer(*args, **kwargs):
  mod = cms.EDProducer('BeamSpotOnlineProducer',
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
