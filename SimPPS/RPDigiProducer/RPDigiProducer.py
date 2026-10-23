import FWCore.ParameterSet.Config as cms

def RPDigiProducer(*args, **kwargs):
  mod = cms.EDProducer('RPDigiProducer',
    RPLandauFluctuations = cms.bool(True),
    RPDisplacementOn = cms.bool(False),
    RPVerbosity = cms.int32(0),
    RPVFATThreshold = cms.double(9000),
    RPTopEdgePosition = cms.double(1.5),
    RPActiveEdgeSmearing = cms.double(0.013),
    RPEquivalentNoiseCharge300um = cms.double(1000),
    RPVFATTriggerMode = cms.int32(2),
    RPInterStripSmearing = cms.vdouble(0.011),
    RPSharingSigmas = cms.double(5),
    RPGeVPerElectron = cms.double(3.61e-09),
    RPActiveEdgePosition = cms.double(0.034),
    RPDeadStripSimulationOn = cms.bool(False),
    ROUList = cms.vstring('TotemHitsRP'),
    RPNoNoise = cms.bool(False),
    RPDigiSimHitRelationsPresistence = cms.bool(False),
    mixLabel = cms.string('mix'),
    RPChargeDivisionsPerThickness = cms.int32(5),
    RPDeltaProductionCut = cms.double(0.120425),
    RPBottomEdgePosition = cms.double(1.5),
    RPBottomEdgeSmearing = cms.double(0.011),
    RPTopEdgeSmearing = cms.double(0.011),
    InputCollection = cms.string('g4SimHitsTotemHitsRP'),
    RPInterStripCoupling = cms.double(1),
    RPDeadStripProbability = cms.double(0.001),
    RPChargeDivisionsPerStrip = cms.int32(15),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
