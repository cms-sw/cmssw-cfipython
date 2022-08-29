import FWCore.ParameterSet.Config as cms

hcalMahiPulseOffsetsGPUESProducer = cms.ESSource('HcalMahiPulseOffsetsGPUESProducer',
  pulseOffsets = cms.vint32(
    -3,
    -2,
    -1,
    0,
    1,
    2,
    3,
    4
  ),
  appendToDataLabel = cms.string('')
)
