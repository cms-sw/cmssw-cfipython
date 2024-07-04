import FWCore.ParameterSet.Config as cms

alpaka_serial_syncHcalRecoParamWithPulseShapeESProducer = cms.ESProducer('alpaka_serial_sync::HcalRecoParamWithPulseShapeESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
