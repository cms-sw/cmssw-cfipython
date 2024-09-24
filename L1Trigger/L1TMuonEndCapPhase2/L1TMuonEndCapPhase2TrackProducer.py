import FWCore.ParameterSet.Config as cms

def L1TMuonEndCapPhase2TrackProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TMuonEndCapPhase2TrackProducer',
    PromptGraphPath = cms.string('L1Trigger/L1TMuonEndCapPhase2/data/prompt_model.pb'),
    DisplacedGraphPath = cms.string('L1Trigger/L1TMuonEndCapPhase2/data/displaced_model.pb'),
    CSCInput = cms.InputTag('simCscTriggerPrimitiveDigisForEMTF'),
    RPCInput = cms.InputTag('rpcRecHitsForEMTF'),
    GEMInput = cms.InputTag('simMuonGEMPadDigiClusters'),
    ME0Input = cms.InputTag('me0TriggerConvertedPseudoDigis'),
    GE0Input = cms.InputTag('ge0TriggerConvertedPseudoDigis'),
    CSCEnabled = cms.bool(True),
    RPCEnabled = cms.bool(True),
    GEMEnabled = cms.bool(True),
    ME0Enabled = cms.bool(True),
    GE0Enabled = cms.bool(False),
    MinBX = cms.int32(-2),
    MaxBX = cms.int32(2),
    BXWindow = cms.int32(1),
    CSCInputBXShift = cms.int32(-8),
    RPCInputBXShift = cms.int32(0),
    GEMInputBXShift = cms.int32(0),
    ME0InputBXShift = cms.int32(-8),
    IncludeNeighborEnabled = cms.bool(True),
    Verbosity = cms.untracked.int32(3),
    ValidationDirectory = cms.string('L1Trigger/L1TMuonEndCapPhase2/data/validation'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
