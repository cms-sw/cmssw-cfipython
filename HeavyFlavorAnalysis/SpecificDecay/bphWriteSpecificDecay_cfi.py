import FWCore.ParameterSet.Config as cms

bphWriteSpecificDecay = cms.EDProducer('BPHWriteSpecificDecay',
  pVertexLabel = cms.string(''),
  patMuonLabel = cms.string(''),
  ccCandsLabel = cms.string(''),
  pfCandsLabel = cms.string(''),
  pcCandsLabel = cms.string(''),
  gpCandsLabel = cms.string(''),
  oniaName = cms.string('oniaCand'),
  sdName = cms.string('kx0Cand'),
  ssName = cms.string('phiCand'),
  buName = cms.string('buFitted'),
  bdName = cms.string('bdFitted'),
  bsName = cms.string('bsFitted'),
  writeVertex = cms.bool(True),
  writeMomentum = cms.bool(True),
  recoSelect = cms.VPSet(
  )
)
