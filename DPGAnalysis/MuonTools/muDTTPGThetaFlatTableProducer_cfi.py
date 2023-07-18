import FWCore.ParameterSet.Config as cms

muDTTPGThetaFlatTableProducer = cms.EDProducer('MuDTTPGThetaFlatTableProducer',
  name = cms.string('ltBmtfInTh'),
  tag = cms.string('BMTF_IN'),
  src = cms.InputTag('bmtfDigis'),
  mightGet = cms.optional.untracked.vstring
)
