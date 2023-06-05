import FWCore.ParameterSet.Config as cms

muDTTPGPhiFlatTableProducer = cms.EDProducer('MuDTTPGPhiFlatTableProducer',
  name = cms.string('ltBmtfIn'),
  tag = cms.string('BMTF_IN'),
  src = cms.InputTag('bmtfDigis'),
  mightGet = cms.optional.untracked.vstring
)
