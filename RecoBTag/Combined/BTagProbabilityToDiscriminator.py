import FWCore.ParameterSet.Config as cms

def BTagProbabilityToDiscriminator(*args, **kwargs):
  mod = cms.EDProducer('BTagProbabilityToDiscriminator',
    discriminators = cms.VPSet(
      cms.PSet(
        denominator = cms.VInputTag(),
        name = cms.string('BvsAll'),
        numerator = cms.VInputTag(
          'pfDeepCSVJetTags:probb',
          'pfDeepCSVJetTags:probbb'
        )
      ),
      cms.PSet(
        denominator = cms.VInputTag(
          'pfDeepCSVJetTags:probc',
          'pfDeepCSVJetTags:probb',
          'pfDeepCSVJetTags:probbb'
        ),
        name = cms.string('CvsB'),
        numerator = cms.VInputTag('pfDeepCSVJetTags:probc')
      ),
      cms.PSet(
        denominator = cms.VInputTag(
          'pfDeepCSVJetTags:probudsg',
          'pfDeepCSVJetTags:probc'
        ),
        name = cms.string('CvsL'),
        numerator = cms.VInputTag('pfDeepCSVJetTags:probc')
      ),
      template = cms.PSetTemplate(
        denominator = cms.VInputTag(),
        numerator = cms.VInputTag(
          'pfDeepCSVJetTags:probb',
          'pfDeepCSVJetTags:probbb'
        ),
        name = cms.string('BvsAll')
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
