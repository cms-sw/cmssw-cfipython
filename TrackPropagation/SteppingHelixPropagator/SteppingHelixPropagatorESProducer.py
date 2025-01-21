import FWCore.ParameterSet.Config as cms

def SteppingHelixPropagatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('SteppingHelixPropagatorESProducer',
    ComponentName = cms.string('SteppingHelixPropagator'),
    NoErrorPropagation = cms.bool(False),
    PropagationDirection = cms.string('alongMomentum'),
    useTuningForL2Speed = cms.bool(False),
    useIsYokeFlag = cms.bool(True),
    endcapShiftInZNeg = cms.double(0),
    SetVBFPointer = cms.bool(False),
    AssumeNoMaterial = cms.bool(False),
    endcapShiftInZPos = cms.double(0),
    useInTeslaFromMagField = cms.bool(False),
    VBFName = cms.string('VolumeBasedMagneticField'),
    useEndcapShiftsInZ = cms.bool(False),
    sendLogWarning = cms.bool(False),
    useMatVolumes = cms.bool(True),
    debug = cms.bool(False),
    ApplyRadX0Correction = cms.bool(True),
    useMagVolumes = cms.bool(True),
    returnTangentPlane = cms.bool(True),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
