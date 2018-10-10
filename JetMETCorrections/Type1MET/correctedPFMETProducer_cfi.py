import FWCore.ParameterSet.Config as cms

correctedPFMETProducer = cms.EDProducer('CorrectedPFMETProducer',
  src = cms.InputTag('pfMet'),
  srcCorrections = cms.VInputTag('corrPfMetType1:type1')
)
