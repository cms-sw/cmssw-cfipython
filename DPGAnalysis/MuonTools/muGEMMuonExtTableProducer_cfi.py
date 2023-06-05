import FWCore.ParameterSet.Config as cms

muGEMMuonExtTableProducer = cms.EDProducer('MuGEMMuonExtTableProducer',
  name = cms.string('muon'),
  src = cms.InputTag('patMuons'),
  fillPropagated = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
