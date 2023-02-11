import FWCore.ParameterSet.Config as cms

GEMDAQStatusSource = cms.EDProducer('GEMDAQStatusSource',
  VFATInputLabel = cms.InputTag('muonGEMDigis', 'VFATStatus'),
  OHInputLabel = cms.InputTag('muonGEMDigis', 'OHStatus'),
  AMCInputLabel = cms.InputTag('muonGEMDigis', 'AMCStatus'),
  AMC13InputLabel = cms.InputTag('muonGEMDigis', 'AMC13Status'),
  AMCSlots = cms.int32(13),
  runType = cms.untracked.string('relval'),
  logCategory = cms.untracked.string('GEMDAQStatusSource'),
  mightGet = cms.optional.untracked.vstring
)
